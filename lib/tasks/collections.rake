namespace :collections do
  desc 'Create and update collections'
  task create: :environment do
    collection_data = [
      { name: 'Chainmail',  skin_api_ids: [1,  2] },
      { name: 'Apprentice', skin_api_ids: [3,  4] },
      { name: 'Rawhide',    skin_api_ids: [5,  6] },
      { name: 'Scallywag',  skin_api_ids: [7,  8] },
      { name: 'Seer',       skin_api_ids: [9, 10] }
    ]

    collection_data.each do |data|
      collection = Collection.find_or_initialize_by(name: data[:name])

      collection.skins = Skin.where(api_id: data[:skin_api_ids])
      collection.note  = data[:note]

      puts collection.name
      collection.save!
    end
  end
end
