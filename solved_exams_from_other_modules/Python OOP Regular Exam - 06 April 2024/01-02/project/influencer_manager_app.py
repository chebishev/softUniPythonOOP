from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    VALID_INFLUENCER_TYPES = {"PremiumInfluencer": PremiumInfluencer,
                              "StandardInfluencer": StandardInfluencer}
    VALID_CAMPAIGN_TYPES = {"HighBudgetCampaign": HighBudgetCampaign,
                            "LowBudgetCampaign": LowBudgetCampaign}

    def __init__(self):
        self.influencers = []
        self.campaigns = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.VALID_INFLUENCER_TYPES:
            return f"{influencer_type} is not an allowed influencer type."
        for influencer in self.influencers:
            if influencer.username == username:
                return f"{username} is already registered."
        self.influencers.append(self.VALID_INFLUENCER_TYPES[influencer_type](username, followers, engagement_rate))
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_CAMPAIGN_TYPES:
            return f"{campaign_type} is not a valid campaign type."
        for campaign in self.campaigns:
            if campaign.campaign_id == campaign_id:
                return f"Campaign ID {campaign_id} has already been created."
        self.campaigns.append(self.VALID_CAMPAIGN_TYPES[campaign_type](campaign_id, brand, required_engagement))
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        try:
            influencer = [i for i in self.influencers if i.username == influencer_username][0]
        except IndexError:
            return f"Influencer '{influencer_username}' not found."

        try:
            campaign = [c for c in self.campaigns if c.campaign_id == campaign_id][0]
        except IndexError:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        payment = influencer.calculate_payment(campaign)
        if payment > 0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= payment
            influencer.campaigns_participated.append(campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        total_reached_followers = {}

        for influencer in self.influencers:
            for campaign in influencer.campaigns_participated:
                reached_followers = influencer.reached_followers(type(campaign).__name__)
                total_reached_followers[campaign] = total_reached_followers.get(campaign, 0) + reached_followers

        return total_reached_followers

    def influencer_campaign_report(self, username: str):
        influencer = [i for i in self.influencers if i.username == username][0]
        return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        output = "$$ Campaign Statistics $$"
        for campaign in sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget)):
            output += "\n" + f"  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)}, Total budget: ${campaign.budget:.2f}, Total reached followers: {self.calculate_total_reached_followers()[campaign]}"

        return output