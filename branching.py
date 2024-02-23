import git

def push_to_main():
    try:
        # Path to your local Git repository
        repo_path = 'https://github.com/vnaidu563/gitbranching.git'

        # Open the repository
        repo = git.Repo(repo_path)

        # Add all files to the index
        repo.index.add('*')

        # Commit changes
        repo.index.commit("Update files")

        # Push changes to the main branch
        origin = repo.remote(name='origin')
        origin.push(refspec='main')

        print("Code successfully pushed to main branch.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    push_to_main()

