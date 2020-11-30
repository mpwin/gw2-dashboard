class Api::SkinsController < ApplicationController
  # GET /skins
  def index
    @skins = Skin.order(:name).where(collection: nil).where.not(name: '')
  end

  # GET /skins/1
  def show
    @skin = Skin.find(params[:id])
  end
end
