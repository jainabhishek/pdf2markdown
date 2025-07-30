
<style>
/* Enhanced PDF-to-Markdown Styles */
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    line-height: 1.6;
    color: #333;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

h1, h2, h3, h4, h5, h6 {
    color: #2c3e50;
    border-bottom: 1px solid #eee;
    padding-bottom: 0.3em;
}

table {
    border-collapse: collapse;
    width: 100%;
    margin: 1em 0;
    border: 1px solid #ddd;
}

th, td {
    border: 1px solid #ddd;
    padding: 12px;
    text-align: left;
}

th {
    background-color: #f8f9fa;
    font-weight: bold;
}

tr:nth-child(even) {
    background-color: #f9f9f9;
}

.page-break {
    page-break-before: always;
    border-top: 2px dashed #ccc;
    margin: 2em 0;
    padding-top: 1em;
}

small {
    font-size: 0.85em;
    color: #666;
}

blockquote {
    border-left: 4px solid #ddd;
    margin: 1em 0;
    padding-left: 1em;
    color: #666;
}

.image-container {
    text-align: center;
    margin: 1em 0;
}

.image-container img {
    max-width: 100%;
    height: auto;
    border: 1px solid #ddd;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
</style>


# Abhishek_Jain_CV___AI_jobs-3

> **Enhanced Conversion** from PDF: `Abhishek_Jain_CV___AI_jobs-3.pdf`  
> Conversion date: 2025-07-29 19:10:32  
> Pages: 5  
> Images extracted: 0  

---


<!-- Page 1 -->

#### Abhishek Jain

#### Mobile : 412-708-8023

#### LinkedIn

#### GitHub

#### Professional Summary

A result-oriented, process and metrics-driven engineering leader with 10+ years of experience in leading and

motivating high performance teams. Passion for crafting a vision and rallying cross-functional teams to deliver

innovations on behalf of customers. Experience in SaaS-based cloud products, consumer internet and other

#### technology products & services for both SMBs and Enterprises.

#### • Skills:

#### Leadership & Process (First-Principles Thinking, SDLC, Agile/Scrum, Cross-Functional

Leadership, Mentoring, LOE Estimation, Jira) AI/ML & LLMs (Context Engineering, RAG,

#### GPT-4o/o3, claude-3-7-sonnet/claude-opus-4, claude-code-sdk, Gemini 2.5 pro, Whisper, AssemblyAI,

LangChain, FAISS, XGBoost, scikit-learn, SMOTE) | Full-Stack Dev (React/Next.js, React Native,

TypeScript, Streamlit, Node.js/Express, Python, Prisma) | Cloud & DevOps (AWS, Azure, Docker,

Kubernetes, CI/CD) | Mobile CI/CD (Firebase App Distribution, automated robot/UI tests, release

gating) | Data & Infra (SQL/PostgreSQL/SQLite/MySQL, NoSQL, ORM/schema design) | Testing &

#### Quality (Jest, Cypress, automated eval frameworks, rigorous code review)

#### Experience

#### Branding Brand Pittsburgh, Pennsylvania

#### •

#### Development Manager II February 2020 - Present

Branding Brand is a company specialising in e-commerce solutions. They create app, web, and store

experiences for hundreds of the world's largest brands in retail, hospitality, and B2B.

#### ◦ AI / ML Engineering (Company-wide Initiatives)

#### ∗

#### AI Assistant - Shipcode

#### ·

#### Built a conversational FQL assistant (React): natural-language→FQL, smart property inference,

coordinated multi-property updates, message-level undo; backed by an internal evaluation harness.

#### ·

Architected and shipped a dedicated AI service (apps/ai-service) with prod endpoints (FQL

#### completion/suggestions, layout assistant, property selector, multi-property updater) powered by

#### OpenAI o3 and gpt-4.1.

#### ·

Implemented an AI-driven layout assistant that converts English to actions on a live component tree

#### and safely executes them.

#### ·

Engineered robust prompt/response schemas (text & JSON), custom parsers, and comprehensive

#### error/timeout handling for predictable latency and graceful recovery.

#### ·

Streamed field metadata/project context for real-time FQL suggestions; added automated test

#### generation, eval frameworks, and logging/monitoring for quality/drift control.

#### ·

#### Implemented model configuration; authored API flow/debugging/implementation docs for fast team

#### adoption.

#### ∗

#### Predict Audit Status - ML for Retail Risk

#### ·

Built an XGBoost classifier to flag high-risk retail batches likely to fail audit (∼7% positive class).

#### ·

#### Engineered 40+ time/order/product features (hour/day/holiday flags, order variance,

#### alcohol/high-value ratios) in an AuditFeatureExtractor.

#### ·

Addressed class imbalance with SMOTE; validated via stratified k-fold CV and

#### ROC-AUC/PR-AUC/F1.

#### ·

Delivered reproducible pipelines with scaling, CLI entry points, model persistence, and data-munging

#### scripts; logged runs to refine thresholds and monitor drift.

#### ∗

#### Smart Cart Analyzer - Multimodal CV & Voice


<!-- Page 2 -->

#### ·

Next.js app auditing Instacart carts: GPT-4o Vision detects items in cart images and compares

#### against expected batch lists to flag missing/unauthorized products.

#### ·

Built an image→structured data pipeline (item, qty, category, confidence) with incremental cart state

#### tracking across multiple images.

#### ·

Added full voice UX (speech commands, ElevenLabs TTS) for hands-free in-store use; exposed REST

#### APIs (/api/analyze-cart, /api/text-to-speech, /api/transcribe) and HEIC→JPEG conversion.

#### ·

Delivered responsive React/TypeScript UI (Tailwind, Framer Motion, dark mode) and real-time

#### pass/fail audit results to reduce shrink and ensure compliance.

#### ∗

#### DevDocs Bot - RAG Documentation Assistant

#### ·

Streamlit app enabling "chat with your docs" via RAG on GPT-4o-mini.

#### ·

Ingested TXT/MD/PDF (PyPDF2), chunked (1k/200 overlap), embedded, and stored vectors in

#### FAISS for fast similarity search.

#### ·

Wired LangChain retrieval chains with conversation memory and streaming responses; built upload

#### sidebar, session history, and robust error fallbacks.

#### ·

#### Documented setup/API key management; modularized codebase for handoff.

#### ∗

#### AbhiScript - AI Transcription Platform

#### ·

#### Full-stack React/Node platform converting large audio files into speaker-labeled transcripts,

#### summaries, and action items.

#### ·

Pipeline: upload → status tracking → AssemblyAI transcription (diarization, chapters) → GPT-4.1

#### speaker/name inference & insight generation → Prisma/SQLite persistence.

#### ·

Hardened backend (Express + TS): JWT auth, rate limiting, Multer uploads, Helmet/CORS,

#### structured logging & error middleware.

#### ·

Modern UX (React, Tailwind, Framer Motion): drag-and-drop uploads, real-time progress, transcript

list/detail views; Whisper STT fallback ensures uptime/cost control; env-driven config with

#### SQLite→Postgres migration path.

#### ◦ Engineering Leadership & Delivery

#### ∗

Modernized company-wide mobile CI/CD: migrated pipelines for all client apps from AppCenter to

Firebase App Distribution, adding automated "robot" UI tests and release gating.

#### ∗

Spearheaded mobile app development for DXL, leading both offshore and onshore development teams,

#### demonstrating effective coordination and leadership skills across diverse geographical locations.

#### ∗

Developed and implemented the Wegmans audit app, designed to monitor Instacart shoppers for excess

and out-of-order items. Introduced a pioneering trust level management system to assign trust scores to

#### shoppers, optimizing audit frequency and improving operational efficiency.

#### ∗

Engaged in hands-on development for both DXL and Wegmans projects, utilizing React Native for

mobile app development alongside Kubernetes, Docker, Minikube, and Node.js for backend services on

Azure. This showcased my versatility in handling both front-end and back-end technologies.

#### ∗

Enhanced code quality and reduced technical debt by providing detailed PR (Pull Request) review

feedback, demonstrating a meticulous approach to code review and a commitment to maintaining high

#### standards of software development.

#### ∗

Worked with a broad range of high-profile clients e.g. Levis, Bed Bath and Beyond, The Related

Companies inc. (Hudson Yard), Theory, Flow Hydration, architecting and implementing project teams to

#### deliver optimal solutions.

#### ∗

Worked with a range of technologies: native projects (DLC employee app, fast retailing; Bed Bath and

Beyond), React Native projects (Levis); CMS migration to Contentstack (Levis); Shopify (Flow

#### Hydration).

#### ∗

Bridged React Native and Native in Bed Bath and Beyond app.

#### ∗

Collaborated with three different teams working, respectively, on Swift (iOS), and Java (Android),

#### React-Native (iOS and Android).

#### ∗

Headed a team of 8 developers (the largest team in the company at that time) to work on a multi-tenant

project(Bed bath and Beyond, Buy Buy Baby and bed bath Canada). This project was delivered on time

#### and within budget.


<!-- Page 3 -->

#### ∗

Developed a flexible and adaptive management style. When the initial technical plan for Bed Bath and

Beyond would have put the project over deadline, I developed and implemented a streamlined approach

which both satisfied project requirements and resulted in timely project delivery.

#### ∗

Developed meticulous approach to detail, in giving detailed level of effort estimations for developers, and

#### offering detailed code level feedback for multiple projects.

#### ∗

Mentoring developers beyond the scope of projects in advancing their careers through regular 1:1

#### meetings.

#### ∗

Quickly and efficiently assimilated technical documentation for a range of projects (including many for

which I was not Engineering Manager) to give detailed and reliable level of effort estimations.

#### Achievements

#### ∗

Solely conceived, built, and deployed all AI/ML initiatives (Shipcode AI Assistant, Predict Audit Status,

Smart Cart Analyzer, DevDocs Bot, AbhiScript) as a one-person team, covering architecture, modeling,

#### infra, UI, and evaluation.

#### ∗

DXL: Drove the end-to-end mobile program, unblocked multi-timezone teams, and instituted code-quality

#### gates that accelerated feature velocity and stabilized releases.

#### ∗

Wegmans: Launched the Instacart audit app with a novel trust-score system, improving audit targeting

#### and operational efficiency.

#### ∗

#### Boosted Levi's deliverable velocity from 60-70% to >100%.

#### ∗

#### Led Levi's expansion to Canada and India.

#### ∗

Managed and delivered the complex multi-tenant Bed Bath & Beyond project on time/in budget; received

#### multiple internal recognitions and a bonus.

#### ∗

Launched first-ever mobile apps for three Fast Retailing brands (Theory, Princess Tam Tam, Comptoir

#### des Cotonniers) with cross-continent coordination.

#### ∗

Drove a >50% revenue increase for Flow Hydration post website launch.

#### Plobal Apps Pune, India

#### •

#### Co-founder and CTO June 2015 - August 2018

Plobal Apps is a SaaS based mobile commerce platform to enable SMBs and Enterprises to generate new

#### mobile revenues, increase conversions, customer loyalty & retention - www.plobalapps.com

◦ Proposed and managed the implementation of a SaaS Mobile Application Development platform, using

which businesses can create a mobile app in < 10 mins without writing any code to help unlock the sales

#### potential by removing the development bottleneck.

◦ Proposed and managed the implementation of complementary products like checkout optimization tool to

#### help increase revenue by cross-selling.

◦ Proposed and managed the implementation of lead generation and automation tool to help the Sales

#### team with refined prospecting.

◦ Created software architecture docs and defined the scope of work for all the development teams.

◦ Provided detailed feedback on wireframes for the design team and finalized the product prototype.

◦ Created technology roadmap, planned weekly sprints and tracked the development progress.

◦ Conducted daily stand-up as scrum master and solved both technical and nontechnical problems.

◦ Reviewed code along with team leads to maintain code quality.

◦ Tracked the progress and constantly motivated the team to make sure that we always release the product

#### on time.

◦ Used tools like Sentry, Crashlytics, etc to track technical issues issues, and performance. Released bug

#### fixes in a timely manner.

◦ Provided fast and effective technical customer support using tools like Freshdesk and closely monitored

user feedback with the technical customer support and customer success teams.


<!-- Page 4 -->

◦ Closely monitored the new technologies, customer feedback, and competition to introduce new features

and third party integration to make sure that our product is the best available option for the customers.

#### Achievements

◦ Hired, motivated and mentored 7 cross-functional teams comprising of software developers, designers,

#### testers, technical customer support.

◦ Plobal Apps became the highest rated mobile app platform on the Shopify app store.

◦ Built 15000+ mobile apps using the platform, for businesses from more than 120 countries.

#### ◦

#### $10

million+ GMV sold on our mobile apps and reached more than 1 million people.

◦ Worked with Google to make Plobal Apps the first mobile app development platform to launch Google

#### Instant apps.

#### ◦ Helped consistently maintain a 5% weekly customer growth.

#### Plobal.com Pune, India

#### •

#### Founding Engineer July 2012 - May 2015

Plobal.com is a consumer internet - social discovery platform to help users find out what's happening [latest

#### offers, discounts, events] at their favorite places in the city

◦ Lead a tech team of frontend and backend developers working on technologies like PHP, MySql,

#### JavaScript, HTML, Objective C and Java for Android.

◦ Worked independently without supervision. Wrote high quality code while providing technical leadership

#### to junior developers.

◦ Reviewed PR and managed releases to staging and production environments.

◦ Responsible for the entire Product Development Lifecycle (ideation, specification, development, release,

#### analysis, and iteration).

#### Achievements

#### ◦ More than 7000 businesses subscribed to the service.

#### ◦ Hired, motivated and mentored 5 cross-functional teams.

◦ Successfully launched the product in 6 months from writing the first line of code.

#### Webricks Pune, India

#### •

#### Co-Founder and President September 2008 - February 2010

Webricks is an IT services company catering to SMBs and Enterprise clients.

◦ Built a platform from scratch to send bulk marketing SMS to mobile users.

◦ Built 30+ web applications which include Inventory Management System for Retail stores, Restaurant

#### Management System, and Quality Control Systems for Financial Research companies.

◦ Built 100+ websites for local businesses and lead the sales effort.

#### Achievements

◦ Made the business profitable with a team of 17 software developers.

#### ◦ Lead product development and sales efforts.

#### Enertiv Inc New York City, New York

#### •

#### Software Development Intern June 2019 - August 2019

#### Enertiv is a real estate technology company.


<!-- Page 5 -->

◦ Implemented Long-Term Degradation profiling in Time Series data (Quadratic Programming).

◦ Implemented Deep Learning models for Equipment classification based on Time Series sensor data.

◦ Proposed and executed image annotation project, supervising annotation workers and provided detailed

#### code feedback.

#### Department of Biomedical Informatics Pittsburgh, Pennsylvania

#### •

#### Student Programmer October 2018 - June 2019

The Department of Biomedical Informatics, University of Pittsburgh School of Medicine.

◦ Implemented Deep Learning and various other Machine Learning methods like Logistic Regression, KNN,

SVM, Extreme Learning Machine, etc on the Physiochemical properties of Protein molecules to predict

#### Ubiquitination sites.

◦ Achieved 3% better accuracy than the published state of the art accuracy.

#### Education

#### University of Pittsburgh Pittsburgh, Pennsylvania

#### •

Master of Science in Information Science, August 2018 - December 2019

#### Courses

#### ◦ Machine Learning

#### ◦ NLP

#### ◦ Computer Vision

#### ◦ Deep Learning (Carnegie Mellon University)

#### ◦ Social Computing

#### ◦ Decision Analysis and Support

#### ◦ Data Analytics

#### Savitribai Phule Pune University (formerly University of Pune) Pune, India

#### •

#### Bachelor of Engineering in Computer Engineering

#### Courses

#### ◦ Machine Learning

#### ◦ Data Structure

#### ◦ Software Engineering

#### ◦ Algorithms

#### ◦ Engineering Mathematics


---

*This document was converted using the Enhanced PDF to Markdown Converter, which preserves layout, styling, and images from the original PDF.*
