from django.core.management.base import BaseCommand
from expenses.models import Expense
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Fill the database with initial data'

    def handle(self, *args, **kwargs):
        USERNAME1 = "testuser1"
        PSWD1 = "testpswd1234"

        USERNAME2 = "testuser2"
        
        # Verificar si la base de datos ya tiene datos
        if Expense.objects.exists():
            self.stdout.write(self.style.SUCCESS('The database already has data.'))
            return

        # Crear un usuario si no existe
        user1, created1 = User.objects.get_or_create(username=USERNAME1, defaults={'password': PSWD1})
        if created1:
            user1.set_password(PSWD1)
            user1.save()

        #USER 2
        user2, created2 = User.objects.get_or_create(username=USERNAME2, defaults={'password': PSWD1})
        if created2:
            user2.set_password(PSWD1)
            user2.save()

        # Crear datos de prueba
        Expense.objects.create(
            title="Night out with GF",
            description="Hamburgers",
            amount=500,
            user=user1,
            created_at="2024-02-15",
            category="food",
        )

        Expense.objects.create(
            title="Nigh out with the boys",
            description="Beer, pizza, paquetaxo",
            amount=200,
            user=user1,
            created_at="2024-02-17",
            category="food",
        )
        
        Expense.objects.create(
            title="Gasoline",
            amount=300,
            user=user1,
            created_at="2024-08-16",
            category="transport",
        )
        
        Expense.objects.create(
            title="New battery",
            amount=3400,
            user=user1,
            created_at="2024-01-03",
            category="transport",
        )
        
        Expense.objects.create(
            title="Tires revision",
            amount=100,
            user=user2,
            created_at="2024-08-16",
            category="transport",
        )
        
        Expense.objects.create(
            title="Medicine",
            description="I got dengue",
            amount=240,
            user=user2,
            created_at="2024-07-31",
            category="health",
        )
        
        Expense.objects.create(
            title="Rent",
            amount=3000,
            user=user1,
            created_at="2024-08-31",
            category="housing",
        )
        
        Expense.objects.create(
            title="Electricity",
            description="Solar panels didn't work",
            amount=4000,
            user=user1,
            created_at="2024-08-12",
            category="housing",
        )
        
        Expense.objects.create(
            title="5th semester inscription",
            amount=3000,
            user=user1,
            created_at="2024-08-9",
            category="education",
        )
        
        Expense.objects.create(
            title="Tequila bottle",
            description="Dad's btdy",
            amount=600,
            user=user1,
            created_at="2024-08-5",
            category="gifts",
        )
        
        Expense.objects.create(
            title="Lost money",
            description="I just found $1, I'M RICH",
            amount=1,
            user=user1,
            created_at="2024-08-14",
            category="savings",
        )
        
        Expense.objects.create(
            title="Viejon's soap",
            amount=60,
            user=user2,
            created_at="2024-07-01",
            category="pets",
        )
        
        Expense.objects.create(
            title="I just last 5 minutes",
            description="If you know you know",
            amount=1500,
            user=user1,
            created_at="2024-07-16",
            category="other",
        )

        Expense.objects.create(
            title="Kdrama movie",
            description="Is for collage I swear",
            amount=200,
            user=user2,
            created_at="2024-08-22",
            category="entretaiment",
        )

        Expense.objects.create(
            title="Suspension for Vocho car mami",
            description="A mexicanada",
            amount=800,
            user=user1,
            created_at="2024-08-22",
            category="transport",
        )
        
        Expense.objects.create(
            title="Luis is sick",
            description="Stupid",
            amount=400,
            user=user1,
            created_at="2024-08-16",
            category="health",
        )

        Expense.objects.create(
            title="Chamba",
            amount=200,
            user=user1,
            created_at="2024-08-21",
            category="other",
        )

        Expense.objects.create(
            title="Chamba",
            amount=200,
            user=user1,
            created_at="2024-08-21",
            category="other",
        )

        self.stdout.write(self.style.SUCCESS('Successfully filled the database with initial data.'))
