import argparse
import git
import sys

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Tag a specific commit in Git and push the tag.')
    parser.add_argument('commit', help='The commit hash to tag.')
    
    # Parse the arguments
    args = parser.parse_args()

    try:
        # Open the repository
        repo = git.Repo(search_parent_directories=True)
        
        # Get the short hash of the commit
        commit = repo.commit(args.commit)
        tag_name = commit.hexsha[:7]  # Use the first 7 characters of the commit hash as the tag name

        # Create and annotate the tag
        tag = repo.create_tag(tag_name, ref=args.commit, message=f"Tagging commit {args.commit}")

        # Push the tag to the remote
        origin = repo.remotes.origin
        origin.push(tag)

        print(f"Successfully created and pushed tag '{tag_name}' on commit {args.commit}")

    except git.exc.GitCommandError as e:
        print(f"Git command error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
