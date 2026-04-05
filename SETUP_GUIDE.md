# FinGuru Setup Guide

## ✅ Current Status

### Services Running:
- **Frontend**: http://localhost:3001/ ✅
- **Backend**: http://localhost:8000/ ✅
- **API Docs**: http://localhost:8000/docs ✅

## ⚠️ Required Configuration

### 1. AWS Credentials (REQUIRED)
You need to configure AWS services in `backend/.env`:

```bash
AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here
AWS_REGION=ap-south-1
```

**How to get AWS credentials:**
1. Go to AWS Console → IAM
2. Create a new user with programmatic access
3. Attach policies: `AmazonS3FullAccess`, `AmazonDynamoDBFullAccess`, `AmazonTextractFullAccess`
4. Copy the Access Key ID and Secret Access Key

### 2. AWS Resources Setup
Run the setup script to create required AWS resources:

```bash
# Windows PowerShell
cd scripts
.\setup-aws.ps1

# Or manually create:
# - S3 Bucket: finguru-uploads
# - DynamoDB Table: finguru-ledger
```

### 3. LLM API Key (At least ONE required)

Edit `backend/.env` and add ONE of these:

**Option 1: OpenRouter (Recommended - has free models)**
```bash
OPENROUTER_API_KEY=your_key_here
```
Get it from: https://openrouter.ai/

**Option 2: OpenAI**
```bash
OPENAI_API_KEY=your_key_here
```
Get it from: https://platform.openai.com/

**Option 3: Groq (Free Whisper transcription)**
```bash
GROQ_API_KEY=your_key_here
```
Get it from: https://console.groq.com/

## 🚀 How to Start the Application

### Start Backend:
```bash
cd backend
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Start Frontend:
```bash
cd frontend
npm run dev
```

## 📝 Features Available

Once configured, you can:
- Upload receipts (requires AWS S3 + Textract)
- Voice transcription (requires OpenAI/Groq API)
- Financial ledger tracking (requires DynamoDB)
- AI financial advisor (requires OpenRouter/OpenAI API)

## 🔧 Troubleshooting

### Backend won't start?
- Check if Python dependencies are installed: `pip install -r requirements.txt`
- Verify `.env` file exists in `backend/` folder

### Frontend won't start?
- Install dependencies: `npm install`
- Check if `.env` file exists in `frontend/` folder

### API calls failing?
- Verify AWS credentials are correct
- Check if AWS resources (S3 bucket, DynamoDB table) exist
- Ensure at least one LLM API key is configured
