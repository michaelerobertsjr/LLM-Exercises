# myPrivateGPT

In this project we will create a way to have a private chat with our documents locally. The application leverages a vector database (using chromadb) that will allow us to ingest our own documents, learn about them, and then we can make queries about the docs.

## Step 1: Setup a new environment

We will create an invironment using `conda` and then install the dependencies so that we don't have dependencies from this project polluting other projects.

```bash
$ conda create -n myPrivateGPT python=3.11
$ conda activate myPrivateGPT
```

## Step 2: install the dependencies
The dependencies are listed in the `requirements.txt` file and can be installed using `pip`:

```
$ pip install -r requirements.txt
```

#### Step 3: Pull the models 

(If you already have models loaded in Ollama, then not required)

```
$ ollama pull mistral
```

#### Step 4: Create a `source_documents` and add documents

Add the folder and then save your document here:

```bash
$ mkdir source_documents
```

#### Step 5: Ingest the files (use python3 if on mac)

 After you have saved documents in the new folder, you can run the following to ingest the documents in the folder (Warning: This may take a few minutes to process):

```
$ python ingest.py
```

Output should look like this:
```shell
Creating new vectorstore
Loading documents from source_documents
Loading new documents: 100%|██████████████████████| 1/1 [00:01<00:00,  1.99s/it]
Loaded 235 new documents from source_documents
Split into 1268 chunks of text (max. 500 tokens each)
Creating embeddings. May take some minutes...
Ingestion complete! You can now run privateGPT.py to query your documents
```

#### Step 6: Run the privateGPT script
```
$ python privateGPT.py
```

##### Step 7: Play with your docs

Enter a query like: How many locations does WeWork have?


### Step 8: Try it with a different model:

```bash
$ ollama pull llama2:13b
$ MODEL=llama2:13b python privateGPT.py
```

## Step 9: Add more files

Put any and all your files into the `source_documents` directory

The supported extensions are:

- `.csv`: CSV,
- `.docx`: Word Document,
- `.doc`: Word Document,
- `.enex`: EverNote,
- `.eml`: Email,
- `.epub`: EPub,
- `.html`: HTML File,
- `.md`: Markdown,
- `.msg`: Outlook Message,
- `.odt`: Open Document Text,
- `.pdf`: Portable Document Format (PDF),
- `.pptx` : PowerPoint Document,
- `.ppt` : PowerPoint Document,
- `.txt`: Text file (UTF-8),

#### Inspired by:

- [privateGPT](https://github.com/imartinez/privateGPT) 
- [ollama](https://github.com/jmorganca/ollama)