Rails.application.routes.draw do
  root 'dashboard#show'

  get '/dyes'    => 'dashboard#show'
  get '/outfits' => 'dashboard#show'

  namespace :api, defaults: { format: :json } do
    resources :collections, only: [:index, :show]
    resources :dyes,        only: [:index, :show]
    resources :outfits,     only: [:index, :show]
    resources :skins,       only: [:index, :show]
  end
end
