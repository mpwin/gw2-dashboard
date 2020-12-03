class Api::DyesController < ApplicationController
  # GET /api/dyes.json
  def index
    @dyes = Dye.order(:name)
  end

  # GET /api/dyes/1.json
  def show
    @dye = Dye.find(params[:id])
  end
end
