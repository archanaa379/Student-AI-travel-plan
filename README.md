# ✈️ TripMate – AI Student Travel Planner

An AI-powered, budget-smart travel planner built specifically for Indian college students.

## 🗂️ Project Structure

```
ai_travel_planner/
├── app.py                  # Streamlit backend (main app)
├── .env                    # API key (never commit to git!)
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Standalone HTML frontend
└── README.md
```

## ⚙️ Setup & Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Set up .env
The `.env` file already contains your API key:
```
OPENAI_API_KEY="your-key-here"
```

### 3. Run the Streamlit App (Recommended)
```bash
streamlit run app.py
```
Opens at: `http://localhost:8501`

### 4. HTML Frontend (Optional)
Open `templates/index.html` directly in a browser.
> Note: The HTML frontend calls OpenAI API directly from browser. For production, use the Streamlit backend to keep your API key secure.

## 🎯 Features
- **Source & Destination** input
- **Budget slider** (₹2,000 – ₹1,00,000) with Indian Rupee formatting
- **Mode of Transport** selector (Train, Bus, Flight, etc.)
- **Interest chips** (Beaches, Street Food, Temples, etc.)
- **Date picker** for travel & return dates
- **AI-generated itinerary** with:
  - Budget breakdown
  - Transport tips (IRCTC, RedBus)
  - Day-by-day plan
  - Student hacks & discounts
  - Must-eat street foods
  - Packing checklist
- **Download itinerary** as text file (Streamlit)
- **Resource links** (Zostel, OYO, Skyscanner, etc.)

## 🔐 Security Note
Never push `.env` or your API key to GitHub. Add `.env` to `.gitignore`.

## 🙏 Inspired By
- GT Holidays
- Zostel & Backpacker India
- IRCTC, RedBus, ixigo
