from app.models import Campaign, CampaignMetrics


def safe_rate(value: float, total: float) -> float:
    if total == 0:
        return 0.0
    return round((value / total) * 100, 2)


def calculate_campaign_metrics(campaign: Campaign) -> CampaignMetrics:
    click_to_registration = safe_rate(campaign.registrations, campaign.clicks)
    registration_to_deposit = safe_rate(
        campaign.first_time_deposits,
        campaign.registrations
    )

    revenue_per_click = 0.0
    if campaign.clicks > 0:
        revenue_per_click = round(campaign.revenue / campaign.clicks, 2)

    roi = 0.0
    if campaign.cost > 0:
        roi = round(((campaign.revenue - campaign.cost) / campaign.cost) * 100, 2)

    suspicious_signal = (
        campaign.clicks > 500
        and campaign.registrations < 10
        and campaign.first_time_deposits == 0
    )

    return CampaignMetrics(
        campaign_id=campaign.campaign_id,
        source=campaign.source,
        geo=campaign.geo,
        click_to_registration_rate=click_to_registration,
        registration_to_deposit_rate=registration_to_deposit,
        revenue_per_click=revenue_per_click,
        roi_percent=roi,
        suspicious_signal=suspicious_signal,
    )
