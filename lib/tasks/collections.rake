namespace :collections do
  desc 'Create and update collections'
  task create: :environment do
    collection_data = {
      'Weapon': [],

      'Armor': {
        'Heavy': [
          { name: 'Banded',           skin_api_ids: [ 54,  55,  83,  84,  87,  104], note: 'Loot' },
          { name: 'Chainmail',        skin_api_ids: [  1,   2,  20,  26,  81, 2041], note: 'Loot' },
          { name: 'Illustrious',      skin_api_ids: [107, 108, 113, 114, 116,  122], note: 'Armorsmith Ascended' },
          { name: 'Reinforced Scale', skin_api_ids: [ 41,  42,  72,  74,  77,  101], note: 'Loot' },
          { name: 'Scallywag',        skin_api_ids: [  7,   8,  27,  33,  38,   92], note: 'Loot' },
          { name: 'Worn Chain',       skin_api_ids: [ 14,  21,  40,  50,  52,   96], note: 'Loot' },
          { name: 'Worn Scale',       skin_api_ids: [ 23,  24,  65,  66,  68,   99], note: 'Loot' },
        ],

        'Medium': [
          { name: 'Marauder',   skin_api_ids: [105, 1697, 1699, 1734, 1772, 1733], note: 'Legacy Armor Reward Track' },
          { name: 'Privateer',  skin_api_ids: [ 44,   46,   75,   76,   80,  102], note: 'Loot' },
          { name: 'Rawhide',    skin_api_ids: [  5,    6,   19,   32,   36,   89], note: 'Loot' },
          { name: 'Rogue',      skin_api_ids: [ 57,   58,   86,   91,  890,  941], note: 'Karma' },
          { name: 'Sneakthief', skin_api_ids: [ 11,   12,   35,   43,   47,   95], note: 'Loot' },
          { name: 'Studded',    skin_api_ids: [ 17,   22,   48,   59, 1719, 1783], note: 'Legacy Armor Reward Track' },
          { name: 'Swindler',   skin_api_ids: [ 28,   31,   60,   67,   71,   97], note: 'Loot' },
        ],

        'Light': [
          { name: 'Apprentice',  skin_api_ids: [  3,   4,  16,  25,  29,  85], note: 'Loot' },
          { name: 'Cabalist',    skin_api_ids: [ 49,  51,  78,  79,  82, 103], note: 'Loot' },
          { name: 'Conjurer',    skin_api_ids: [ 62,  63,  88,  90,  93, 106], note: 'Loot' },
          { name: 'Country',     skin_api_ids: [ 13,  18,  53,  56,  64,  98], note: 'Loot' },
          { name: 'Illustrious', skin_api_ids: [109, 110, 115, 118, 119, 123], note: 'Tailor Ascended' },
          { name: 'Magician',    skin_api_ids: [ 34,  37,  69,  70,  73, 100], note: 'Loot' },
          { name: 'Seer',        skin_api_ids: [  9,  10,  30,  39,  45,  94], note: 'Loot' }
        ]
      }
    }

    collection_data[:Weapon].each do |data|
      save_collection('Weapon', data)
    end

    collection_data[:Armor].each do |weight_class, collections|
      collections.each do |data|
        save_collection('Armor', data, weight_class)
      end
    end
  end
end

def save_collection(category, data, weight_class = nil)
  collection = Collection.find_or_initialize_by(
    name:         data[:name],
    category:     category,
    weight_class: weight_class
  )

  collection.skins = Skin.where(api_id: data[:skin_api_ids])
  collection.note  = data[:note]

  puts collection.name
  collection.save!
end
