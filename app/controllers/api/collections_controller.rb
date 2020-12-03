class Api::CollectionsController < ApplicationController
  # GET /api/collections.json
  def index
    @collections = Collection.order(:name)
  end

  # GET /api/collections/1.json
  def show
    @collection = Collection.find(params[:id])
  end
end
