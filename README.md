# Legal Assistant

This project leverages the InLegalBERT model to automate the processing and analysis of legal documents, enhancing efficiency for legal professionals in India. The model is designed to extract relevant information, summarize key points, and classify various types of legal documents.

**Team name**: DREAM TEAM<br>

**Team Members**<br>
Member 1: Najiya Nazrin CN - Mar Athanasius College of engineering, Kothamagalam
Member 2: Bineesha K P -  Mar Athanasius College of engineering, Kothamagalam
Member 3: Janeesha Devi R- Mar Athanasius College of engineering, Kothamagalam

**Hosted Project Link**<br>
https://github.com/najiya101/legal-assistant-.git

**Project Description**<br>
This project uses the InLegalBERT model to automate the analysis and processing of legal documents, streamlining tasks for legal professionals in India. It is designed to extract important details, summarize key points, and classify different types of legal documents, improving efficiency and accuracy in legal workflows.

**The Solution**<br>
We are  creating a legal assistant chatbot by training it with legal data to answer questions and explain terms in simple language. The website cum chatbot is designed to be user-friendly, giving personalized advice while offering helpful resources for law students and advocates. It's like having a tech-savvy legal assistant who makes understanding the law fun and easy!

## Features<br>
_**Document Classification**: Automatically classifies documents into categories such as contracts, legislation, or court cases.
- **Named Entity Recognition**: Identifies important entities (e.g., parties involved, dates) within legal texts.
- **Semantic Segmentation**: Segments documents into functional parts (e.g., facts, arguments) for easier navigation [1][2].

1.  **Install required libraries:**<br>
      bash
   pip install transformers torch
   
**2. Load the model and tokenizer:**<br>
   python
   from transformers import AutoTokenizer, AutoModel

   tokenizer = AutoTokenizer.from_pretrained("law-ai/InLegalBERT")
   model = AutoModel.from_pretrained("law-ai/InLegalBERT")
   
**3. Usage Example**<br>
To process a legal document:
python
text = "Insert your legal text here."
encoded_input = tokenizer(text, return_tensors="pt")
output = model(**encoded_input)
last_hidden_state = output.last_hidden_state


 ### Applications<br>
- **Legal Research**: Assists in navigating large volumes of legal texts efficiently.
- **Contract Review**: Automates the review process by highlighting key clauses and potential issues.
- **Regulatory Compliance**: Provides insights to ensure adherence to relevant laws and regulations.

## Technologies Used<br>
- Backend: Python
- Frontend: HTML, JavaScript
- Model: InLegal BERT
- Libraries: Transformers, jason,pypdf2,Fast API, sk-learn, nltk.tokenize,numpy,torch,

  
### Conclusion<br>
The Legal Document Assistant utilizing InLegalBERT significantly enhances the capabilities of legal professionals by automating tedious tasks and improving access to critical information in legal texts. This project exemplifies the integration of advanced NLP models in the legal domain to streamline workflows and enhance productivity

## Screenshots


<div>

  <img src="https://github.com/user-attachments/assets/f8c94d43-90c9-4448-979c-82dee2d34533" alt="Initial State" height="500"/>  
  <img src="https://github.com/user-attachments/assets/ee083a7f-8557-492b-bc29-d0f68365ac79" alt="Queen's Placed" height="500"/>
  <img src="https://github.com/user-attachments/assets/587d368e-a5a7-495a-b8f9-6e0bc8682fc2" height="500"/>


  <img src="https://github.com/user-attachments/assets/aa78c8b2-71ae-4873-95dd-5b8c516197f6" height="500"/>

</div>
##video

link: https://drive.google.com/drive/folders/1DiI-kot_28L-Gb5ycKQHc7G6w4bltQPd

**Team Contributions**<br>
Najiya Nazrin C N : BERT model fine tuning & document summarization <br>
Bineesha K P: Backend developer(API development)<br>
Janeesha Devi R: UI/UX Design <br>
