# Hosting a Professional Resume on a Static Website

## Purpose

This README guide provides step-by-step instructions on how to host a professional resume using Markdown, a static site generator, and a forge with static site hosting capabilities. These instructions are designed for individuals with basic computer skills who are interested in learning modern technical documentation techniques as described in Andrew Etter's book, "Modern Technical Writing." By following this guide, you will create and publish a professional online presence that showcases your resume while implementing industry-standard documentation practices.

## Prerequisites

Before getting started, you'll need:

1. **A Markdown-formatted resume** - Your professional resume formatted in Markdown syntax
2. **Git** - Version control system installed on your local machine
   - [Download Git](https://git-scm.com/downloads)
3. **Python** - Required to run the Pelican static site generator
   - [Download Python](https://www.python.org/downloads/) (Version 3.7 or higher recommended)
4. **Text Editor** - Any text editor for working with Markdown files
   - Recommended: [Visual Studio Code](https://code.visualstudio.com/) with Markdown extensions
5. **GitHub Account** - For hosting your repository and static website
   - [Sign up for GitHub](https://github.com/join)
6. **Command Line Interface** - Basic knowledge of using terminal/command prompt

## Instructions

### 1. Create Your Resume Using Markdown

Etter emphasizes the importance of using lightweight markup languages in his book because they are simple, portable, and easily versionable. Markdown perfectly embodies these principles as it's human-readable even in its raw form.

To create your resume in Markdown:

1. Open your text editor of choice
2. Format your resume using Markdown syntax
3. Save the file as `resume.md`

Markdown allows you to focus on content rather than formatting, which aligns with Etter's principle of prioritizing content accessibility over complex formatting.

### 2. Set Up a Local Repository with Git

Etter strongly advocates for distributed version control systems because they enable collaboration, provide a history of changes, and facilitate content updates. Git is the industry standard that embodies these principles.

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

This version control approach ensures your content is trackable and recoverable at any point, which is a fundamental principle Etter emphasizes for sustainable documentation.

### 3. Install and Configure Pelican

Etter recommends using static site generators because they convert lightweight markup into modern, responsive websites without the complexity of databases or server-side processing. Pelican is a Python-based static site generator that works seamlessly with Markdown.

To install Pelican:

1. Ensure Python and pip are installed
2. Run the following command to install Pelican and Markdown support:
   ```
   pip install pelican markdown
   ```
3. Navigate to your project directory in the command line
4. Run `pelican-quickstart` to initialize your Pelican project
5. Answer the prompts to configure your site:
   - Set the title for your website (e.g., "Professional Portfolio")
   - Enter your name as the author
   - Accept default language (en)
   - Select "No" for URL prefix if you're using GitHub Pages
   - Accept default settings for other options or customize as desired

Pelican implements Etter's principle of separating content from presentation, allowing you to focus on writing quality content in Markdown while the generator handles the HTML production.

### 4. Organize Your Content

Etter emphasizes the importance of well-organized documentation structure. For a resume site, this means organizing your content in a way that's intuitive and accessible.

1. In your project directory, locate the `content` folder created by Pelican
2. Move your `resume.md` file into this folder
3. Add a title, date, and category metadata to the top of your resume file:
   ```
   Title: Resume
   Date: 2025-03-02
   Category: Professional
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

Static site generation converts your Markdown content into HTML, which can be hosted anywhere. Etter favors this approach because it creates fast, secure, and portable websites.

1. From your project directory, run:
   ```
   pelican content
   ```
2. This generates your website in the `output` directory
3. To preview your site locally, run:
   ```
   pelican --listen
   ```
4. Open your browser and navigate to `http://localhost:8000`

This step demonstrates Etter's principle of using automation to create consistent, error-free documentation outputs.

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

This step follows Etter's principle of making documentation publicly accessible and versionable.

### 7. Set Up GitHub Pages

Etter emphasizes the importance of making documentation accessible online. GitHub Pages provides free hosting for static sites directly from your repository.

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
   git add docs
   git commit -m "Add built site for GitHub Pages"
   git push
   ```

This approach demonstrates Etter's principle of publishing documentation where users can easily access it.

### 8. Update and Maintain Your Resume Site

Etter emphasizes that documentation is never "done" and should be regularly updated. To maintain your resume site:

1. Make changes to your Markdown files as needed
2. Regenerate your site with `pelican content -o docs -s publishconf.py`
3. Commit and push your changes:
   ```
   git add .
   git commit -m "Update resume information"
   git push
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

Markdown is better than raw HTML for documentation because it's significantly more readable and writable for humans. As Etter points out in his book, lightweight markup languages like Markdown allow content creators to focus on writing rather than formatting. With Markdown, you can create structured documents using simple, intuitive syntax without getting lost in HTML tags. This aligns with Etter's principle that documentation should be easy to create and maintain. Additionally, Markdown is portable across platforms and can be easily converted to various output formats including HTML, PDF, and more.

### I changed the Markdown version of my resume, but the changes don't appear on my website. Why?

This happens because static site generators don't automatically rebuild your site when you change source files. After making changes to your Markdown files, you need to regenerate your site by running `pelican content -o docs -s publishconf.py` and then commit and push these changes to GitHub. This two-step process (generating HTML and then updating the repository) is part of the static site workflow that Etter describes. It gives you more control over when updates are published, allowing you to review changes before they go live. Remember that GitHub Pages may also take a few minutes to reflect your changes after pushing.

### How do I add images to my resume site?

To add images to your resume site, first place the image files in the `content/images` directory of your Pelican project. Then, in your Markdown files, reference the images using Markdown syntax: `![Alt text](/images/filename.jpg)`. When Pelican generates your site, it will correctly link these images. This approach follows Etter's recommendation of organizing assets logically within your documentation project.

### Why use a static site instead of a service like LinkedIn?

As Etter emphasizes, static websites offer several advantages over third-party platforms: they give you complete control over your content's presentation, they don't depend on a third party's continued existence, they're faster to load, more secure (no databases to hack), and they demonstrate your technical skills to potential employers. While LinkedIn is valuable for networking, a personal static site showcases your ability to implement modern technical practices—exactly the kind of initiative that can distinguish you from other candidates.

## Credits

- Hui Miao - Original resume content and implementation
- Andrew Etter - Principles of modern technical writing
- Pelican - Static site generator
- GitHub - Repository hosting and GitHub Pages
- [Your peer review group members' names] - Peer review and feedback
- University of Manitoba - Assignment framework and guidance

*This README was created as part of COMP 2600: Technical Communication in Computer Science at the University of Manitoba, Winter 2025.*
