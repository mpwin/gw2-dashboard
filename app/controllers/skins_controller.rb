class SkinsController < ApplicationController
  before_action :set_skin, only: [:show, :edit, :update, :destroy]

  # GET /skins
  # GET /skins.json
  def index
    @skins = Skin.all
  end

  # GET /skins/1
  # GET /skins/1.json
  def show
  end

  # GET /skins/new
  def new
    @skin = Skin.new
  end

  # GET /skins/1/edit
  def edit
  end

  # POST /skins
  # POST /skins.json
  def create
    @skin = Skin.new(skin_params)

    respond_to do |format|
      if @skin.save
        format.html { redirect_to @skin, notice: 'Skin was successfully created.' }
        format.json { render :show, status: :created, location: @skin }
      else
        format.html { render :new }
        format.json { render json: @skin.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /skins/1
  # PATCH/PUT /skins/1.json
  def update
    respond_to do |format|
      if @skin.update(skin_params)
        format.html { redirect_to @skin, notice: 'Skin was successfully updated.' }
        format.json { render :show, status: :ok, location: @skin }
      else
        format.html { render :edit }
        format.json { render json: @skin.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /skins/1
  # DELETE /skins/1.json
  def destroy
    @skin.destroy
    respond_to do |format|
      format.html { redirect_to skins_url, notice: 'Skin was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_skin
      @skin = Skin.find(params[:id])
    end

    # Only allow a list of trusted parameters through.
    def skin_params
      params.require(:skin).permit(:name)
    end
end
