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

# I get the content of the file
file_info = repo.get_contents(file_path)
original_content = file_info.decoded_content.decoded("utf-8")

# I now replaces all the "Andrews" in the file with my name
updated_content = original_content.replace("Andrew", my_name)

