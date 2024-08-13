from project.influencers.base_influencer import BaseInfluencer


class StandardInfluencer(BaseInfluencer):

    def calculate_payment(self, campaign: object):
        return campaign.budget * 0.45

    def reached_followers(self, campaign_type):
        if campaign_type == "HighBudgetCampaign":
            return int(self.followers * self.engagement_rate * 1.2)
        elif campaign_type == "LowBudgetCampaign":
            return int(self.followers * self.engagement_rate * 0.9)

