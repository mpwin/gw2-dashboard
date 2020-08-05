namespace :api do
  namespace :account do
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
