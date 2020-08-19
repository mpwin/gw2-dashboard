class Collection < ApplicationRecord
  has_many :skins, before_add: :get_skin_attributes,
                   after_add:  :set_unlocked

  validates_presence_of :name, :category

  def update_unlocked
    update(unlocked: skins.pluck(:unlocked).all?(true))
  end

  private

  def get_skin_attributes(skin)
    update(category: skin.category, weight_class: skin.weight_class)
  end

  def set_unlocked(skin)
    update_unlocked
  end
end
