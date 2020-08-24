class Skin < ApplicationRecord
  belongs_to :collection, optional: true

  validates_presence_of :api_id

  serialize :flags,        Array
  serialize :restrictions, Array

  after_save :update_collection_unlocked, if: [:saved_change_to_unlocked, :collection]

  private

  def update_collection_unlocked
    collection.update_unlocked
  end
end
