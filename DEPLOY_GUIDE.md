# 🚀 ContextIQ Deployment Guide

## Deployment Options

### Option 1: Streamlit Cloud (Recommended - FREE!)

#### Prerequisites
- GitHub account
- Groq API key
- (Optional) Tavily API key
- (Optional) LangSmith API key

#### Step-by-Step

1. **Push to GitHub**
```bash
git init
git add .
git commit -m "Initial commit - ContextIQ with all features"
git branch -M main
git remote add origin https://github.com/yourusername/contextiq.git
git push -u origin main
```

2. **Deploy on Streamlit Cloud**

a. Go to [share.streamlit.io](https://share.streamlit.io/)

b. Click "New app"

c. Select your repository: `yourusername/contextiq`

d. Set main file path: `app.py`

e. Click "Advanced settings"

f. Add your secrets:
```toml
GROQ_API_KEY = "gsk_your_actual_key"
TAVILY_API_KEY = "tvly_your_actual_key"  # Optional
LANGSMITH_API_KEY = "ls_your_actual_key"  # Optional
```

g. Click "Deploy"

h. Wait 2-3 minutes for deployment

i. Your app is live! 🎉

**Your app URL will be:**
`https://yourusername-contextiq-app-randomid.streamlit.app`

---

### Option 2: Docker Deployment

#### Create Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Create .streamlit directory
RUN mkdir -p .streamlit

# Expose port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

#### Build and Run

```bash
# Build image
docker build -t contextiq .

# Run container with environment variables
docker run -p 8501:8501 \
  -e GROQ_API_KEY="your_key" \
  -e TAVILY_API_KEY="your_key" \
  -e LANGSMITH_API_KEY="your_key" \
  contextiq
```

#### Docker Compose (docker-compose.yml)

```yaml
version: '3.8'

services:
  contextiq:
    build: .
    ports:
      - "8501:8501"
    environment:
      - GROQ_API_KEY=${GROQ_API_KEY}
      - TAVILY_API_KEY=${TAVILY_API_KEY}
      - LANGSMITH_API_KEY=${LANGSMITH_API_KEY}
    volumes:
      - ./conversations.db:/app/conversations.db
    restart: unless-stopped
```

Run with:
```bash
docker-compose up -d
```

---

### Option 3: AWS EC2

#### 1. Launch EC2 Instance

- AMI: Ubuntu 22.04 LTS
- Instance type: t2.medium (or t2.micro for testing)
- Security group: Allow ports 22 (SSH) and 8501 (Streamlit)

#### 2. Connect and Setup

```bash
# SSH into instance
ssh -i your-key.pem ubuntu@your-ec2-ip

# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and pip
sudo apt install python3-pip python3-venv -y

# Clone repository
git clone https://github.com/yourusername/contextiq.git
cd contextiq

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create secrets file
mkdir -p .streamlit
nano .streamlit/secrets.toml
# Add your API keys and save

# Run with nohup (background)
nohup streamlit run app.py --server.port=8501 --server.address=0.0.0.0 &
```

#### 3. Access Your App

Visit: `http://your-ec2-ip:8501`

#### 4. Optional: Setup Nginx Reverse Proxy

```bash
# Install Nginx
sudo apt install nginx -y

# Configure Nginx
sudo nano /etc/nginx/sites-available/contextiq
```

Add:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

```bash
# Enable site
sudo ln -s /etc/nginx/sites-available/contextiq /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

Now accessible at: `http://your-domain.com`

---

### Option 4: Heroku

#### 1. Create Heroku App

```bash
# Install Heroku CLI
curl https://cli-assets.heroku.com/install.sh | sh

# Login
heroku login

# Create app
heroku create your-contextiq-app

# Set buildpack
heroku buildpacks:set heroku/python
```

#### 2. Create Procfile

```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

#### 3. Create setup.sh

```bash
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

#### 4. Update requirements.txt

Add at the end:
```
gunicorn==20.1.0
```

#### 5. Deploy

```bash
# Set environment variables
heroku config:set GROQ_API_KEY="your_key"
heroku config:set TAVILY_API_KEY="your_key"
heroku config:set LANGSMITH_API_KEY="your_key"

# Deploy
git push heroku main

# Open app
heroku open
```

---

### Option 5: Google Cloud Run

#### 1. Prepare for Cloud Run

Create `Dockerfile`:
```dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV PORT=8080

CMD streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

#### 2. Deploy

```bash
# Install Google Cloud SDK
# Then authenticate
gcloud auth login

# Set project
gcloud config set project YOUR_PROJECT_ID

# Build and deploy
gcloud run deploy contextiq \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars GROQ_API_KEY="your_key",TAVILY_API_KEY="your_key"
```

---

## Environment Variables Setup

For all deployment options, you need these environment variables:

### Required
```
GROQ_API_KEY=gsk_your_groq_api_key_here
```

### Optional (for full features)
```
TAVILY_API_KEY=tvly_your_tavily_key_here
LANGSMITH_API_KEY=ls_your_langsmith_key_here
```

---

## Post-Deployment Checklist

After deploying, verify:

- [ ] App loads successfully
- [ ] Can select all 4 models
- [ ] Can send messages and get responses
- [ ] Streaming works (if enabled)
- [ ] Conversations save to database
- [ ] Can browse conversation history
- [ ] Web search works (if API key added)
- [ ] Can download user guide PDF
- [ ] Can export conversations
- [ ] Copy/regenerate buttons work
- [ ] Theme toggle works

---

## Monitoring & Maintenance

### Streamlit Cloud
- View logs in Streamlit Cloud dashboard
- Monitor app health
- Check resource usage
- Update via git push

### Docker
```bash
# View logs
docker logs contextiq

# Restart container
docker restart contextiq

# Update app
git pull
docker-compose up -d --build
```

### EC2
```bash
# Check app status
ps aux | grep streamlit

# View logs
cat nohup.out

# Restart app
pkill -f streamlit
nohup streamlit run app.py &
```

---

## Scaling Considerations

### For High Traffic:

1. **Use Multiple Instances**
   - Deploy on multiple servers
   - Use load balancer

2. **Optimize Database**
   - Consider PostgreSQL instead of SQLite
   - Add database indexes
   - Implement connection pooling

3. **Cache Responses**
   - Add Redis caching
   - Cache common queries
   - Reduce API calls

4. **Rate Limiting**
   - Implement user rate limits
   - Protect against abuse
   - Monitor API usage

---

## Security Best Practices

1. **API Keys**
   - Never commit secrets to git
   - Use environment variables
   - Rotate keys regularly

2. **HTTPS**
   - Always use HTTPS in production
   - Get SSL certificate (Let's Encrypt)
   - Enforce HTTPS redirects

3. **Access Control**
   - Add authentication if needed
   - Implement user management
   - Monitor access logs

4. **Database**
   - Regular backups
   - Encrypt sensitive data
   - Secure file permissions

---

## Troubleshooting Deployment Issues

### App Won't Start
- Check Python version (3.8+)
- Verify all dependencies installed
- Check environment variables set
- Review error logs

### Slow Performance
- Upgrade instance size
- Optimize database queries
- Enable caching
- Use CDN for static assets

### Database Issues
- Check file permissions
- Ensure directory writable
- Verify SQLite installed
- Consider cloud database

### API Errors
- Verify API keys valid
- Check API rate limits
- Monitor API status pages
- Implement retry logic

---

## Cost Estimates

### Streamlit Cloud
- **FREE** for public apps
- 1GB resources
- Unlimited users
- Community support

### AWS EC2
- **t2.micro:** FREE tier eligible
- **t2.small:** ~$17/month
- **t2.medium:** ~$34/month
- Plus data transfer costs

### Heroku
- **Free:** $0/month (limited dyno hours)
- **Hobby:** $7/month
- **Standard:** $25/month

### Google Cloud Run
- **Pay per use:** ~$5-20/month
- Free tier: 2M requests/month
- Auto-scaling included

---

## Recommended Deployment

**For Personal Use:**
→ Streamlit Cloud (FREE)

**For Team/Company:**
→ AWS EC2 with Nginx + SSL

**For Enterprise:**
→ Google Cloud Run or AWS with auto-scaling

---

## Getting Help

If deployment fails:

1. Check deployment logs
2. Verify environment variables
3. Test locally first
4. Review specific platform docs
5. Check GitHub Issues

---

**Happy Deploying! 🚀**
