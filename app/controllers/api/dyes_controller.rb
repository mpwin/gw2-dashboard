class Api::DyesController < ApplicationController
  # GET /dyes
  def index
    @dyes = Dye.order(:name)
  end

  # GET /dyes/1
  def show
    @dye = Dye.find(params[:id])
  end
end
