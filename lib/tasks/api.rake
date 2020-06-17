namespace :api do
  namespace :skins do
    desc 'Get skins'
    task get: :environment do
      url = 'https://api.guildwars2.com/v2/skins'
      uri = URI(url)
      res = Net::HTTP.get(uri)
      ids = JSON.parse(res)

      ids.each_slice(200) do |slice|
        uri = URI("#{url}?ids=#{slice.join(',')}")
        res = Net::HTTP.get(uri)

        JSON.parse(res).each do |skin|
          Skin.create(name: skin['name'])
        end

        sleep(2)
      end
    end
  end
end
