class CreateCollections < ActiveRecord::Migration[6.0]
  def change
    create_table :collections do |t|
      t.string  :name
      t.boolean :unlocked, default: false
      t.text    :note
    end
  end
end
