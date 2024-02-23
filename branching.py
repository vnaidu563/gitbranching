import git

def add_new_feature():
    # Add your new feature implementation here
    print("New feature added!")

def push_to_main():
    try:
        # Path to your local Git repository
        repo_path = 'https://github.com/vnaidu563/gitbranching.git'

        # Open the repository
        repo = git.Repo(repo_path)

        # Add all files to the index
        repo.index.add('*')

        # Commit changes
        repo.index.commit("Update files with new feature")

        # Push changes to the main branch
        origin = repo.remote(name='origin')
        origin.push(refspec='main')

        print("Code successfully pushed to main branch.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    add_new_feature()
    push_to_main()


