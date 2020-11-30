Rails.application.routes.draw do
  root 'dashboard#show'
  
  get '/outfits' => 'dashboard#show'

  resources :collections
  resources :skins
end
