Rails.application.routes.draw do
  root 'dashboard#show'
  
  resources :collections
  resources :skins
end
