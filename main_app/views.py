from django.shortcuts import render



# Add the Cat class & list and view function below the imports
class Dream:  # Note that parens are optional if not inheriting from another class
  def __init__(self, title, description, date, type):
    self.title = title
    self.description = description
    self.date = date
    self.type = type

dreams = [
  Dream('Lion chases me', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at', 'Today.','nightmare'),
  Dream('I fly', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at', 'june 3', 'recurring'),
  Dream('Im not myself', 'bombLorem ipsum dolor sit amet, consectetur adipiscing elit. Proin atay', 'Some day', 'weird'),
  Dream('teeth fell, again', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at rex', '06/08/23', 'Nightmare')
]


# Create your views here.
# Define the home view
def home(request):
  return render(request, 'home.html')

def dream_index(request):
  return render(request, 'dreams/index.html', {'dreams':dreams} )