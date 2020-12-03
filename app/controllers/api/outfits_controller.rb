class Api::OutfitsController < ApplicationController
  # GET /api/outfits.json
  def index
    @outfits = Outfit.order(:name)
  end

  # GET /api/outfits/1.json
  def show
    @outfit = Outfit.find(params[:id])
  end
end
