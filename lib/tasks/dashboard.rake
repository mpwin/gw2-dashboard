namespace :dashboard do
  desc 'Update all data'
  task :refresh do
    Rake::Task['api:skins:get'].invoke
    Rake::Task['api:account:skins:get'].invoke
    Rake::Task['collections:create'].invoke
  end
end
