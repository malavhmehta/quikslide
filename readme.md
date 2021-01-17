## Inspiration

**Quikslide** was ideated through a common problem that we had all faced in the past - creating effective slideshows under time constraints. Each team member agreed that a AI-Powered Presentation Generator that adaptively created slides based on an input script would be useful in many use cases, and thus Quikslide was born.

## What it does

Quikslide uses multiple refined APIs in delivering the final product, a complete slideshow, into your hands. The app first takes in speech input, either typed from your own notes, or spoken directly into the browser and processed through _web speech_. The app then summarizes and tokenizes text in order to come up with headers and body text (bullet points) for slides, and searches web browsers for relevant images to use as guidance for each slide. The presentation is created, designed, and shared with the user for further usage and alteration. We don't want to impede the creative process, but rather help the users on their way. On average, an employee uses approximately 10 hours to create a slideshow. By using our service, they are able to optimize out the tedious portions, allowing them to make beautful and dynamic presentations in the fraction of the time.

## How we built it

We first use the Chrome Adaptive Speech Recognition API to understand the users input. By processing the speech using the Azure Language Analytics Engine and the Azure Cognitive Engine, we are able to categorize data. We also integrated NLTK alongside the Azure Cognitive API to deliver precise and accurate text summarization. We then take this tokenized and summarized data to create lively slideshows using the Google Sides and Google Drive API. Then by using the Bing Search API, we are able to use our custom image searching algorithm to deliver precise and relevant images. By building our app with the Flask web-server, we are able to deliver high performance web throughput while creating a dynamic dashboard. We also used Flask-Login, SQLAlchemy, Jinja2, and NLP for the backend, and we used Html+CSS+jQuery to create the frontend.

## Challenges we ran into

As like any challenge, we faced any difficulties with a dynamic mindset. We had never used many of the technologies we needed to make our app a reality and it was a challenge to bring together unknown APIs in a limited time frame to create the final product. Specifically, we had issues with managing API call limits—such as the Google Drive share API—and with creating the summarization functions on our own with NLP, a library none of us had experience with. We also faced challenges tweaking the NLP Algorithms to deliver on high-precision analysis.

## Accomplishments that we're proud of

Quikslide's functionality is admirable for the early-stage development it has undergone. It can effectively seperate slides and categorize their titles based off of contextual tokenization that is done throughout the process. The slideshows are coherent and the formatting of the slide is consistent without overflows, or collisions. We're quite proud of the backend that was programmed on a really short time constraint, and we're confident that we're able to improve it for future purposes.

## Accomplishments that we're proud of

Quikslide's functionality is admirable for the early-stage development it has undergone. It can effectively seperate slides and categorize their titles based off of contextual tokenization that is done throughout the process. The slideshows are, for the most part, coherent and the formatting of the slide is consistent without overflows, and collisions. We're quite proud of the backend that was programmed on a really short time constraint, and we're confident that we're able to improve it for future purposes.

## What we learned

The biggest lessons we learned were the importance of being flexible with the scope of our project and altering it in favor of time and resource constraints.

We also learned:

- Flask
- SQLAlchemy
- Jinja
- NLP (text summarization, keyword extraction)
- Working with Azure Cognitive APIs
- Working with the Google Docs and Slides APIs
- Limiting API calls to avoid exceeding limits
- Working with Domains and DNS
- Power of working in a team

## What's next for QuikSlide

We're excited to expand QuikSlide by increasing the configurations and slide templates that can be produced by our application. For example, we're looking to expand the theming available for our slideshows and adding company specific theming that adheres to design guidelines as well as expanding the generated content, through the addition of more variable templating and adding functionality for graphs and custom images. We also want to expand the natural language processing component so we can create more impactful slides—such as slides that focus on numbers—as well as more concisely shorten the summary of the script and automatically make bullet points more grammatically correct. Our vision for Quikslide is for it to become a product used by millions worldwide and which saves billions of hours of time and resources.
