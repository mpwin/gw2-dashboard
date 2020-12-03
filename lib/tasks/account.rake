namespace :api do
  namespace :account do
    namespace :dyes do
      desc 'Get account dyes'
      task get: :environment do
        uri = URI::HTTPS.build(
          host: 'api.guildwars2.com',
          path: '/v2/account/dyes',
          query: { access_token: Rails.application.credentials.api_key }.to_query
        )
        response = Net::HTTP.get(uri)

        JSON.parse(response).each do |id|
          dye = Dye.find_by(api_id: id)

          dye.unlocked = true

          puts "UNLOCK -- #{dye.api_id}, #{dye.name}" if dye.changed?

          dye.save!
        end
      end
    end

    namespace :outfits do
      desc 'Get account outfits'
      task get: :environment do
        uri = URI::HTTPS.build(
          host: 'api.guildwars2.com',
          path: '/v2/account/outfits',
          query: { access_token: Rails.application.credentials.api_key }.to_query
        )
        response = Net::HTTP.get(uri)

        JSON.parse(response).each do |id|
          outfit = Outfit.find_by(api_id: id)

          outfit.unlocked = true

          puts "UNLOCK -- #{outfit.api_id}, #{outfit.name}" if outfit.changed?

          outfit.save!
        end
      end
    end

    namespace :skins do
      desc 'Get account skins'
      task get: :environment do
        uri = URI::HTTPS.build(
          host: 'api.guildwars2.com',
          path: '/v2/account/skins',
          query: { access_token: Rails.application.credentials.api_key }.to_query
        )
        response = Net::HTTP.get(uri)

        JSON.parse(response).each do |id|
          skin = Skin.find_by(api_id: id)

          skin.unlocked = true

          puts "UNLOCK -- #{skin.api_id}, #{skin.name}" if skin.changed?

          skin.save!
        end
      end
    end
  end
end
