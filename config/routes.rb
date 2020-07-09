Rails.application.routes.draw do
  root 'dashboard#show'
  resources :skins
end
