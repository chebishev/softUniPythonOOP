from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):

    def calculate_payment(self, campaign: object):
        return campaign.budget * 0.85

    def reached_followers(self, campaign_type):
        if campaign_type == "HighBudgetCampaign":
            return int(self.followers * self.engagement_rate * 1.5)
        elif campaign_type == "LowBudgetCampaign":
            return int(self.followers * self.engagement_rate * 0.8)
