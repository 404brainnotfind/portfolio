# Hosting a Professional Resume on a Static Website

## Purpose

This README guide provides step-by-step instructions on how to host a professional resume using Markdown, a static site generator, and a forge with static site hosting capabilities. By following Andrew Etter’s principles from Modern Technical Writing, you will create and publish a professional online presence that showcases your resume while implementing industry-standard documentation practices.

## Prerequisites

Before getting started, you'll need:

1. **A Markdown-formatted resume** - Your professional resume formatted in Markdown syntax
2. **Git** - Version control system installed on your local machine
   - [Download Git](https://git-scm.com/downloads)
3. **Python** - Required to run the Pelican static site generator
   - [Download Python](https://www.python.org/downloads/) (Version 3.7 or higher recommended)
4. **Pelican** - Python-based static site generator 
5. **Text Editor** - Any text editor for working with Markdown files
   - Recommended: [Visual Studio Code](https://code.visualstudio.com/) with Markdown extensions
6. **GitHub Account** - For hosting your repository and static website
   - [Sign up for GitHub](https://github.com/join)
7. **Command Line Interface** - Basic knowledge of using terminal/command prompt

## Instructions

### 1. Create Your Resume Using Markdown

#### Why Markdown

Markdown lets you focus on content over formatting, which Etter says is key for maintainable documentation.

To create your resume in Markdown:

1. Open your text editor of choice
2. Write your resume using Markdown syntax (e.g., `# Header`, `- List items`). 
3. Save the file as `resume.md`

### 2. Set Up a Local Repository with Git

Etter highlights Git as essential for modern technical writing. Initialize a Git repository to track revisions of your resume, ensuring you can review changes or revert mistakes easily.

To initialize your repository:

1. Create a new folder for your project on your computer
2. Open your command line interface
3. Navigate to your project folder using the `cd` command
4. Run `git init` to initialize a new Git repository
5. Create an initial commit with your resume:
   ```
   git add resume.md
   git commit -m "Add resume in Markdown format"
   ```

This version control approach ensures your content is trackable and recoverable at any point.

### 3. Install and Configure Pelican
Pelican, a Python-based static site generator, align with Etter’s principle of automating repetitive tasks. Install Pelican to convert your Markdown resume into a fast, secure website without manual HTML coding.

To install Pelican:


1. Run the following command to install Pelican and Markdown support:
   ```
   pip install pelican markdown
   ```
2. Navigate to your project directory in the command line
3. Run `pelican-quickstart` to initialize your Pelican project
4. Answer the prompts to configure your site:
   - Enter your name as the author
   - Set the title for your website (e.g., "Professional Portfolio")
   - URL Prefix: https://YourGitHubUsername.github.io/Portfolio
   - Enable GitHub Pages: Type Y 
   - Press Enter for the rest prompts to use default values.



### 4. Organize Your Content

Etter advises organizing documentation intuitively. Move your resume.md to Pelican’s content folder and create a homepage (index.md) to guide visitors naturally to your resume.

1. locate the `content` folder created by Pelican
2. Move your `resume.md` file into this folder
3. Add a title, date, and category metadata to the top of your resume file:
   ```
   Title: Resume
   Date: 2025-03-02
   ```
4. Create an `index.md` file in the content folder to serve as your homepage:
   ```
   Title: About Me
   Date: 2025-03-02
   Save_as: index.html
   
   Welcome to my professional portfolio. Here you can find information about my background, skills, and experience.
   
   [View my resume](/resume.html)
   ```

This structure follows Etter's principle of organizing documentation logically and making navigation intuitive for users.

### 5. Generate Your Static Site

Static site generation converts your Markdown content into HTML, which can be hosted anywhere. As Etter recommends, preview your site locally to ensure accuracy. Static generation avoids server-side risks and ensures your resume loads quickly for all users.

1. From your project directory, run:
   ```
   pelican content
   ```
2. To preview your site locally, run:
   ```
   pelican --listen
   ```
3. Open your browser and navigate to `http://localhost:8000`
4. Repeat step 1-3 if you modify anything in content

### 6. Create a Repository on GitHub

Etter recommends using public version control platforms (forges) to host documentation because they provide visibility, enable collaboration, and integrate with modern workflows. 

1. Log in to your GitHub account
2. Click the "+" icon in the upper right corner and select "New repository"
3. Name your repository (e.g., "professional-portfolio")
4. Make it public
5. Do not initialize with a README (we already have one)
6. Click "Create repository"
7. Follow the instructions to push your existing repository:
   ```
   git remote add origin https://github.com/yourusername/professional-portfolio.git
   git branch -M main
   git push -u origin main
   ```

???
### 7. Set Up GitHub Pages

Etter emphasizes the importance of making documentation accessible online. Push changes to GitHub to keep your online resume current.

1. In your GitHub repository, go to "Settings"
2. Scroll down to the "GitHub Pages" section
3. Under "Source", select the branch where your site is located (usually "main")
4. Select the "docs" folder or "root" depending on your setup
5. Click "Save"
6. Modify your pelican configuration in `publishconf.py` to work with GitHub Pages
7. Build your site for production by running:
   ```
   pelican content -o docs -s publishconf.py
   ```
8. Commit and push these changes:
   ```
   ghp-import output -b gh-pages
   git push origin gh-pages
   ```

This approach demonstrates Etter's principle of publishing documentation where users can easily access it.

### 8. Update and Maintain Your Resume Site

Etter emphasizes that documentation is never "done" and should be regularly updated. To maintain your resume site:

1. Make changes to your Markdown files as needed
2. Push Source Code to main Branch
   ```
   git add .
   git push origin main
   ```
3.Regenerate your site with `pelican content -o docs -s publishconf.py`
4. Deploy Site to gh-pages Branch:
   ```
   ghp-import output -b gh-pages
   git push origin gh-pages
   ```

This ongoing maintenance process aligns with Etter's philosophy that documentation should be treated as a living product that evolves over time.

## Resources

For further exploration and learning, check out these resources:

1. [Andrew Etter's Modern Technical Writing](https://www.amazon.com/Modern-Technical-Writing-Introduction-Documentation-ebook/dp/B01A2QL9SS) - The definitive guide on modern documentation approaches
2. [GitHub Markdown Guide](https://guides.github.com/features/mastering-markdown/) - Comprehensive Markdown tutorial
3. [The Markdown Guide](https://www.markdownguide.org/) - In-depth resource for learning Markdown syntax
4. [Pelican Documentation](https://docs.getpelican.com/) - Official documentation for the Pelican static site generator
5. [Git Handbook](https://guides.github.com/introduction/git-handbook/) - Essential Git commands and workflows
6. [GitHub Pages Documentation](https://docs.github.com/en/pages) - Complete guide to GitHub Pages features

## FAQ

### Why is Markdown better than writing raw HTML?

Markdown is better than raw HTML for documentation because it's significantly more readable and writable for humans. 

As Etter points out in his book, lightweight markup languages like Markdown allow content creators to focus on writing rather than formatting. 

With Markdown, you can create structured documents using simple, intuitive syntax without getting lost in HTML tags. This aligns with Etter's principle that documentation should be easy to create and maintain.

Additionally, Markdown is portable across platforms and can be easily converted to various output formats including HTML, PDF, and more.

### I changed the Markdown version of my resume, but the changes don't appear on my website. Why?

This happens because static site generators don't automatically rebuild your site when you change source files. 

After making changes to your Markdown files, you need to regenerate your site by running `pelican content -o docs -s publishconf.py` and then commit and push these changes to GitHub. Remember that GitHub Pages may also take a few minutes to reflect your changes after pushing.

### How do I add images to my resume site?

To add images to your resume site, first place the image files in the `content/images` directory of your Pelican project. 

Then, in your Markdown files, reference the images using Markdown syntax: `![Alt text](/images/filename.jpg)`. When Pelican generates your site, it will correctly link these images. 

### Why use a static site instead of a service like LinkedIn?

As Etter emphasizes, static websites offer several advantages over third-party platforms: they give you complete control over your content's presentation, they don't depend on a third party's continued existence, they're faster to load, more secure (no databases to hack), and they demonstrate your technical skills to potential employers. 

While LinkedIn is valuable for networking, a personal static site showcases your ability to implement modern technical practices—exactly the kind of initiative that can distinguish you from other candidates.

## Credits

- Andrew Etter - Principles of modern technical writing
- Pelican - Static site generator
- GitHub - Repository hosting and GitHub Pages
- Maro Hamed/Shuvo Sarker/Zelong Yang - Peer review and feedback
- University of Manitoba - Assignment framework and guidance
- favicon.io - favicon icon
- simple-bootstrap -  Pelican theme used for website design

*This README was created as part of COMP 2600 at the University of Manitoba, Winter 2025.*
