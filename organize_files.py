# Importing libraries that we will use.
import shutil
import os
# Creating a dictionary using paths as keys and a list of extensions associated with it as values.
EXTENSION_CATEGORIES = {
    'C:\Writer': ['doc', 'docx', 'odt'],
    'C:\Calc': ['xlsx', 'ods', 'csv'],
    'C:\Impress': ['pptx', 'odp'],
    'C:\PDF': ['pdf'],
    'C:\Executáveis': ['exe', 'msi'],
    r'C:\Users\Lorran\Pictures': ['png', 'jpeg', 'jpg'],
    'C:\Compactados': ['zip', 'rar'],
    r'C:\Users\Lorran\Music': ['ogg', 'mp3'],
    r'C:\Users\Lorran\Videos': ['wmv', 'mp4', 'mkv']
}
def get_extension(item):
  extensao = item.split(".")[-1] # With [-1] you are accessing the last element of the resulting list after dividing the file name, in this case the divider is ".".
  return extensao
# Inserting a function called organizer and defining 'directory' as an argument.
def organizer(directory):
  if not os.path.exists(directory):
    # I could create a directory if it not-exists using os.makedirs(directory).
    print('non-existent directory') #I chose to display this message.
  # Creating a list from a directory that i want.
  file_list = os.listdir(directory)
# Now I will go through this list.
  for item in file_list:
    # Using a method called join to fusion the path of the directory with the item.
    path = os.path.join(directory,item)
    # Checking if the path formed by the directory and the item(file) corresponds to a file.
    if os.path.isfile(path):
      # Creating a variable whitch her value is the method 'get_extension'.
      extension = get_extension(item)
      # Here i going through the dictionary
      for destination, extensions in EXTENSION_CATEGORIES.items(): # destination is the paths(keys), extensions is the extensions associated with them , i use the method '.items() to go through the dictionary considering the pair key-value like one unique thing.
        if extension in extensions:
          # Creating a variable called new_path and assign it with the fusion of the path and the item
          new_path = os.path.join(destination,item)
          # Here i moving the path(ex: C:\Users\User\Downloads\file.docx -> C:\Writer\file.docx')
          shutil.move(path, new_path)
          # Once the file has been moved, it is not necessary to check other categories
          break
    else:
        # if i not have files in my target directory this message will be displayed.
        print("No such file here my friend!")

if __name__ == '__main__': # when you see this condition in a Python script it means that the code inside the block that follows will only be executed when you run the script directly (i.e. not when it is imported as a module)
  # Import OS librarie
  import os

  # Create a variable called user_profile_directory  and assign it with the user's home directory regardless of operating system.
  user_profile_directory = os.path.expanduser("~")
  # join the directory path of the current user and join it with the directory Downloads
  directory = os.path.join(user_profile_directory, 'Downloads')
  # We call the 'organizer' method and pass the directory as an argument.
  organizer(directory)
  # If the program is ok this message will be displayed.
  print('SUCCESSFUL WORK SON!')

