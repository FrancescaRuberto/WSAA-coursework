from github import Github
from config import apiKey

# Configuration of my name and repository
# I created a new public repository with a file called test.txt in it
my_name = "Francesca"
repository_name = "FrancescaRuberto/Miscellaneous"
file_path = "test.txt"

# I add the key already "hidden"
g = Github(apiKey)
repo = g.get_repo(repository_name)

