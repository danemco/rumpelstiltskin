from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from pygments import highlight
from pygments.formatters import HtmlFormatter as Formatter

SUPPORTED_LANG = (
    ('HTMLDjango', 'Django HTML Templtates'),
    ('Python', 'Python'),
    ('Html', 'HTML'),
    ('Plain', 'Plain Text'),
)

# Create your models here.
class Bin(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField('pasted contents in plain text')
    html_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, blank=True, null=True)
    language = models.CharField(max_length=30, choices=SUPPORTED_LANG, default='Plain')

    def __unicode__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('binpaste:detail', args=(self.id,))

    def save(self, *args, **kwargs):
        self.html_text = syntaxify(self.text, self.language)
        super(Bin, self).save(*args, **kwargs)

def syntaxify(text, language):
    if language == 'Python':
        from pygments.lexers import PythonLexer as Lexer
    elif language == 'Html':
        from pygments.lexers import HtmlLexer as Lexer
    elif language == 'HTMLDjango':
        from pygments.lexers import HtmlDjangoLexer as Lexer
    else:
        from pygments.lexers import TextLexer as Lexer

    html = highlight(text, Lexer(), Formatter(linenos='table'))
    return html
    
