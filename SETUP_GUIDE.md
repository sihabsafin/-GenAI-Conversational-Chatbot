# 🚀 ContextIQ Setup Guide

## Step-by-Step Installation & Configuration

### 1️⃣ Prerequisites

Before you begin, ensure you have:
- ✅ Python 3.8 or higher installed
- ✅ pip (Python package manager)
- ✅ A Groq API account (free tier available)

### 2️⃣ Installation Steps

#### A. Clone or Download the Project

```bash
# If using git
git clone <repository-url>
cd ContextIQ-Conversational-Chatbot

# Or download and extract the ZIP file
```

#### B. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- streamlit - Web UI framework
- langchain - LLM framework
- langchain-groq - Groq integration
- langsmith - Conversation tracing
- tavily-python - Web search
- sqlalchemy - Database ORM
- fpdf2 - PDF generation

#### C. Set Up API Keys

1. **Create the secrets file:**

```bash
# Create .streamlit directory if it doesn't exist
mkdir -p .streamlit

# Copy the template
cp .streamlit/secrets.toml.template .streamlit/secrets.toml
```

2. **Get your Groq API Key (REQUIRED):**

   a. Visit [Groq Console](https://console.groq.com/)
   
   b. Sign up for a free account
   
   c. Navigate to "API Keys" section
   
   d. Click "Create API Key"
   
   e. Copy the key (starts with `gsk_`)
   
   f. Open `.streamlit/secrets.toml` and paste:
   ```toml
   GROQ_API_KEY = "gsk_your_actual_key_here"
   ```

3. **Get Tavily API Key (OPTIONAL - for web search):**

   a. Visit [Tavily.com](https://tavily.com/)
   
   b. Sign up for free account
   
   c. Get your API key from dashboard
   
   d. Add to secrets.toml:
   ```toml
   TAVILY_API_KEY = "tvly_your_actual_key_here"
   ```

4. **Get LangSmith API Key (OPTIONAL - for tracing):**

   a. Visit [LangSmith](https://smith.langchain.com/)
   
   b. Sign up for account
   
   c. Go to Settings → API Keys
   
   d. Create new API key
   
   e. Add to secrets.toml:
   ```toml
   LANGSMITH_API_KEY = "ls_your_actual_key_here"
   ```

#### D. Run the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### 3️⃣ Verify Installation

1. **Check if all models work:**
   - Try selecting each model from the dropdown
   - Send a test message
   - All 4 models should respond

2. **Test streaming:**
   - Enable "Streaming Responses" in sidebar
   - Send a message
   - You should see the response appear word-by-word

3. **Test conversation history:**
   - Send a few messages
   - Click "New Chat"
   - Your previous conversation should appear in the sidebar
   - Click on it to load it back

4. **Test web search (if enabled):**
   - Enable "Web Search" checkbox
   - Ask a current events question
   - Response should include web search results

5. **Test PDF download:**
   - Click "Download User Guide (PDF)"
   - A PDF should download with the complete guide

### 4️⃣ Features Checklist

After setup, verify these features work:

- [ ] **Multi-Model Support** - All 4 models selectable and working
- [ ] **Streaming Responses** - Text appears progressively
- [ ] **Conversation History** - Chats saved and loadable
- [ ] **Web Search** - Real-time web results (if API key added)
- [ ] **LangSmith Tracing** - Traces visible in dashboard (if API key added)
- [ ] **Copy Button** - Can copy any response
- [ ] **Regenerate Button** - Can regenerate last response
- [ ] **Export TXT** - Can download conversation as text
- [ ] **Export JSON** - Can download conversation as JSON
- [ ] **PDF Guide** - Can download user guide PDF
- [ ] **Theme Toggle** - Can switch between dark/light
- [ ] **Search Conversations** - Can search through saved chats

### 5️⃣ Common Issues & Solutions

#### Issue: "GROQ_API_KEY not found"
**Solution:** 
- Ensure `.streamlit/secrets.toml` exists
- Check the file has `GROQ_API_KEY = "your_key"`
- Restart the Streamlit app

#### Issue: "Model not found" error
**Solution:**
- All models are now properly configured
- If still getting errors, check Groq dashboard for model availability
- Try switching to a different model

#### Issue: "Web search not working"
**Solution:**
- Add TAVILY_API_KEY to secrets.toml
- Enable the "Web Search" checkbox in sidebar
- Check Tavily dashboard for API quota

#### Issue: "Database errors"
**Solution:**
- Delete `conversations.db` file
- Restart the application
- Database will be recreated

#### Issue: "Streaming not working"
**Solution:**
- Ensure checkbox is enabled
- Clear browser cache
- Restart Streamlit app

### 6️⃣ Directory Structure

After setup, your project should look like:

```
ContextIQ/
├── .streamlit/
│   ├── config.toml              # Streamlit configuration
│   ├── secrets.toml             # Your API keys (keep private!)
│   └── secrets.toml.template    # Template for API keys
├── assets/
│   ├── style-dark.css          # Dark theme
│   └── style-light.css         # Light theme
├── app.py                       # Main application
├── llm_engine.py               # LLM handling
├── database.py                 # Database operations
├── web_search.py               # Web search integration
├── pdf_generator.py            # PDF generation
├── requirements.txt            # Dependencies
├── README.md                   # Main documentation
├── SETUP_GUIDE.md             # This file
└── conversations.db           # SQLite database (created automatically)
```

### 7️⃣ Next Steps

Once everything is working:

1. **Customize the System Prompt:**
   - Open the "System Prompt" expander in sidebar
   - Modify the AI's behavior and personality

2. **Experiment with Settings:**
   - Try different temperature values
   - Adjust max token length
   - Test different models for different tasks

3. **Start Using:**
   - Ask coding questions
   - Get writing help
   - Research with web search
   - Save important conversations

4. **Deploy (Optional):**
   - Deploy to Streamlit Cloud (free)
   - Share with others
   - See DEPLOY_GUIDE.md for details

### 8️⃣ Getting Help

If you encounter issues:

1. Check this setup guide
2. Review README.md troubleshooting section
3. Check the Streamlit app logs in terminal
4. Verify API keys are correct
5. Ensure all dependencies installed
6. Try restarting the application

### 9️⃣ Best Practices

- **API Keys:** Never commit secrets.toml to version control
- **Backups:** Export important conversations regularly
- **Updates:** Keep dependencies updated with `pip install -r requirements.txt --upgrade`
- **Database:** Back up `conversations.db` file periodically

### 🔟 Success!

If you can:
- ✅ Send messages and get responses
- ✅ See conversations in sidebar
- ✅ Download the user guide PDF
- ✅ Switch between models
- ✅ Copy and regenerate responses

Then you're all set! Enjoy using ContextIQ! 🎉

---

**Need more help?** Check out:
- README.md for feature details
- Groq documentation: https://console.groq.com/docs
- LangChain docs: https://python.langchain.com/
- Streamlit docs: https://docs.streamlit.io/
