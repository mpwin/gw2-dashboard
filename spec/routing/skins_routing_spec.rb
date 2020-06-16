require "rails_helper"

RSpec.describe SkinsController, type: :routing do
  describe "routing" do
    it "routes to #index" do
      expect(get: "/skins").to route_to("skins#index")
    end

    it "routes to #new" do
      expect(get: "/skins/new").to route_to("skins#new")
    end

    it "routes to #show" do
      expect(get: "/skins/1").to route_to("skins#show", id: "1")
    end

    it "routes to #edit" do
      expect(get: "/skins/1/edit").to route_to("skins#edit", id: "1")
    end


    it "routes to #create" do
      expect(post: "/skins").to route_to("skins#create")
    end

    it "routes to #update via PUT" do
      expect(put: "/skins/1").to route_to("skins#update", id: "1")
    end

    it "routes to #update via PATCH" do
      expect(patch: "/skins/1").to route_to("skins#update", id: "1")
    end

    it "routes to #destroy" do
      expect(delete: "/skins/1").to route_to("skins#destroy", id: "1")
    end
  end
end
