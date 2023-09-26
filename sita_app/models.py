
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class User(AbstractUser):
    is_administrateur=models.BooleanField(default=False)
    is_help_desk=models.BooleanField(default=False)
    is_consulteur =models.BooleanField(default=True)


class Site(models.Model):

    site_id = models.AutoField(primary_key=True)
    code_IATTA = models.CharField(max_length=20)
    nom_site = models.CharField(max_length=20,unique=True)

    class Meta:
        unique_together = ('site_id', 'code_IATTA')
    def __str__(self):
            return self.nom_site
    
class Comptoir(models.Model):

    comptoir_Id = models.AutoField(primary_key=True)
    comptoir_name=models.CharField(max_length=20)
    site = models.ForeignKey('Site', on_delete=models.CASCADE, null=False )

class Compagnie(models.Model):
     compagnie_id = models.AutoField(primary_key=True)
     nom_compagnie =models.CharField(max_length=20,unique=True)
     site=models.ForeignKey(Site,on_delete=models.CASCADE)
     class Meta:
        unique_together = ('nom_compagnie', 'site')
     def __str__(self):
            return self.nom_compagnie
 
class Zone(models.Model):
    nom_zone= models.CharField(max_length=20,primary_key=True)
    site=models.ForeignKey(Site,on_delete=models.CASCADE)
    def __str__(self):
        return self.nom_zone
    
class Terminal(models.Model):
    nom_terminal= models.CharField(max_length=50,primary_key= True )
    site=models.ForeignKey(Site,on_delete=models.CASCADE)
    def __str__(self):
        return self.nom_terminal

class Equipement(models.Model):
    nom_equipement = models.CharField(max_length=50, unique=True)
    quantite = models.IntegerField(default=0)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_equipement


class Ticket(models.Model):
    id_ticket = models.AutoField(primary_key=True)
    TYPE_INC = [
        ('problem', 'Problem'),
        ('change', 'Change'),
        ('incident', 'Incident'),
    ]
    TYPE_INT = [
        ('P', 'panne'),
        ('V', 'visite de maintenance'),
        ('AL', 'amenagement lourd'),
        ('I', 'installation'),
        ('D', 'drivers'),
        ('F', 'formation'),
    ]
    NATURE_INT = [
        ('P', 'preventif'),
        ('C', 'curatif'),
        ('M', 'modification'),
        ('TN', 'travaux neufs'),
    ]
    TYPE_COM = [
        ('T', 'telephone'),
        ('L', 'local'),
    ]

    etat_ticket=[
        ('o','ouvert'),
        ('f','ferme'),
        ('a','annule'),
    ]
    # Your other fields and choices here

    # Declare h_debut and h_cloture fields as DateTimeFields
    # h_debut = models.DateTimeField(auto_now_add=True)
    # h_cloture = models.DateTimeField(null=True, blank=True)

    # Duration of the incident
    # incident_duration = models.DurationField(null=True, blank=True)
    site = models.ForeignKey(Site,on_delete=models.CASCADE)
    compagnie = models.ForeignKey(Compagnie, on_delete=models.CASCADE)
    terminal = models.ForeignKey(Terminal,on_delete=models.CASCADE)
    zone = models.ForeignKey( Zone, on_delete=models.CASCADE )
    equipement = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE_INC)
    type_intervention = models.CharField(max_length=20, choices=TYPE_INT)
    nature_int = models.CharField(max_length=20, choices=NATURE_INT)
    type_communication = models.CharField(max_length=20, choices=TYPE_COM)
    probleme = models.CharField(max_length=20,null=True) # no choices here because we need to allow more in later versions ! 
    solution = models.CharField(max_length=100,null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    etat=models.CharField(max_length=20, choices=etat_ticket)
    closed_at= models.DateTimeField(null=True)

        # # Calculate and set the incident duration
        # if self.h_debut and self.h_cloture:
        #     self.incident_duration = self.h_cloture - self.h_debut
        # else:
        #     self.incident_duration = None
    def save(self, *args, **kwargs):

        # Check if it's a 'problem' type and an equipement is associated
        if self.type == 'probleme' and self.equipement:
            if self.equipement.quantite > 0:
                self.equipement.quantite -= 1  # Reduce by 1
                self.equipement.save()

        super().save(*args, **kwargs)
