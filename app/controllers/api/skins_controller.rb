class Api::SkinsController < ApplicationController
  # GET /api/skins.json
  def index
    @skins = Skin.order(:name).where(collection: nil).where.not(name: '')
  end

  # GET /api/skins/1.json
  def show
    @skin = Skin.find(params[:id])
  end
end
