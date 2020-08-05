class Skin < ApplicationRecord
  belongs_to :collection, optional: true

  serialize :flags,        Array
  serialize :restrictions, Array

  after_save :set_collection_unlock, if: [:saved_change_to_unlocked, :collection]

  def set_collection_unlock
    if collection.skins.pluck(:unlocked).all?(true)
      collection.update!(unlocked: true)
    else
      collection.update!(unlocked: false)
    end
  end
end
