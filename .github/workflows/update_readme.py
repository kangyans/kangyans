import yaml

# Read the YAML file
with open('_config.yml', 'r') as file:
    config = yaml.safe_load(file)

# Read the current README
with open('README.md', 'r') as file:
    readme = file.readlines()

# Find the Blog Posts section in the README
start_line = readme.index("## Blog Posts\n")
end_line = start_line
for i in range(start_line + 1, len(readme)):
    if readme[i].startswith("## "):
        end_line = i
        break

# Generate the new Blog Posts section
new_blog_posts = ["## Blog Posts\n"]
for post in config['blog_posts']:
    new_blog_posts.append(f"### [{post['title']}]({post['url']})\n")
    new_blog_posts.append(f"{post['description']}\n\n")

# Update the README
readme = readme[:start_line] + new_blog_posts + readme[end_line:]
with open('README.md', 'w') as file:
    file.writelines(readme)
