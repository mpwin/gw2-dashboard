class Api::OutfitsController < ApplicationController
  # GET /outfits
  def index
    @outfits = Outfit.order(:name)
  end

  # GET /outfits/1
  def show
    @outfit = Outfit.find(params[:id])
  end
end
