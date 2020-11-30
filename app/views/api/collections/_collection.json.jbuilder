json.extract! collection, :id, :name, :category, :weight_class, :unlocked, :note
json.url api_collection_url(collection, format: :json)
