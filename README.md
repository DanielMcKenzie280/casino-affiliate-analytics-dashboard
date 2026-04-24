# Casino Affiliate Analytics Dashboard

A lightweight analytics dashboard for tracking iGaming affiliate traffic, conversions, deposits, revenue, and campaign performance.

This project helps affiliate marketers and casino-related platforms understand which traffic sources generate real value, detect suspicious traffic patterns, and compare campaign ROI using simple metrics and visual reports.

## Features

- Track clicks, registrations, first-time deposits, and revenue
- Calculate conversion rate, CPA, ROI, and estimated player value
- Compare campaigns, traffic sources, and GEO performance
- Detect suspicious traffic patterns such as high clicks with no conversions
- Provide API endpoints for analytics data
- Includes sample data for quick testing

## Use Cases

- iGaming affiliate performance monitoring
- Casino campaign reporting
- Traffic quality analysis
- Conversion funnel optimization
- Basic fraud and fake-traffic detection

## Tech Stack

- Python
- FastAPI
- Pydantic
- JSON sample data

## Getting Started

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
