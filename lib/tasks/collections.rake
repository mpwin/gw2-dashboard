namespace :collections do
  desc 'Create and update collections'
  task create: :environment do
    collection_data = [
      { name: 'Chainmail',  skin_api_ids: [ 1,  2, 20], note: 'Loot' },
      { name: 'Apprentice', skin_api_ids: [ 3,  4, 16], note: 'Loot' },
      { name: 'Rawhide',    skin_api_ids: [ 5,  6, 19], note: 'Loot' },
      { name: 'Scallywag',  skin_api_ids: [ 7,  8],     note: 'Loot' },
      { name: 'Seer',       skin_api_ids: [ 9, 10],     note: 'Loot' },
      { name: 'Sneakthief', skin_api_ids: [11, 12],     note: 'Loot' },
      { name: 'Country',    skin_api_ids: [13, 18],     note: 'Loot' },
      { name: 'Worn Chain', skin_api_ids: [14, 21],     note: 'Loot' },
      { name: 'Studded',    skin_api_ids: [17],         note: 'Legacy Armor Reward Track' }
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
