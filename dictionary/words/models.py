from django.db import models

class PhyrexianWord(models.Model):
    phyrexian = models.CharField(max_length=255)
    official = models.CharField(max_length=255)
    latin = models.CharField(max_length=255)
    ipa = models.CharField(max_length=255)
    definition = models.CharField(max_length=255)

    def __str__(self):
        return self.official + '(' + self.definition + ')'

class PhyrexianWordNotes(models.Model):
    phyrexian_word = models.ForeignKey(PhyrexianWord, on_delete=models.CASCADE, related_name='notes')
    notes = models.TextField()
    def __str__(self):
        return self.notes[:25] + '...'

class CompositeBridge(models.Model):
    child = models.ForeignKey(PhyrexianWord, on_delete=models.RESTRICT, related_name='child_relationships')
    parent = models.ForeignKey(PhyrexianWord, on_delete=models.RESTRICT, related_name='parent_relationships')
    def __str__(self):
        return 'Parent: ' + self.parent.__str__() + ', Child: ' + self.child.__str__()

class Card(models.Model):
    card_name = models.CharField(max_length=255)
    def __str__(self):
        return self.card_name

class ExampleText(models.Model):
    card = models.ForeignKey(Card, on_delete=models.RESTRICT,related_name='texts')
    text_field = models.CharField(max_length=255)
    phyrexian_text = models.TextField()
    english_text = models.TextField()
    def __str__(self):
        return self.card.__str__() + ' ' + self.text_field + ': ' + self.english_text

class ExampleBridge(models.Model):
    phyrexian_word = models.ForeignKey(PhyrexianWord, on_delete = models.RESTRICT,related_name='bridges')
    example_text = models.ForeignKey(ExampleText, on_delete = models.RESTRICT,related_name='bridges')
    def __str__(self):
        return 'Word: ' + self.phyrexian_word.__str__() + ', Example: ' + self.example_text.__str__()
