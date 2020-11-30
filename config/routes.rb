Rails.application.routes.draw do
  root 'dashboard#show'

  get '/outfits' => 'dashboard#show'

  defaults format: :json do
    resources :collections, only: [:index, :show]
  end

  resources :skins
end
